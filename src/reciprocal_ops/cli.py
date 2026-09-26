"""
Production Command Line Interface Wrapper for Reciprocal Operations (reciprocal-ops).
"""

import sys
import os
import argparse
from reciprocal_ops.telemetry.hydrator import SyntheticHydrator
from reciprocal_ops.telemetry.json_parser import JSONStreamParser
from reciprocal_ops.telemetry.spike_detector import TelemetrySpikeDetector
from reciprocal_ops.pipeline.webwork_assessor import WebworkScore
from reciprocal_ops.pipeline.alert_classifier import AlertClassifier
from reciprocal_ops.pipeline.debt_broker import DebtBroker
from reciprocal_ops.storage.record_buffer import HistoricalRecordBuffer

def handle_scan(args):
    """Executes an ingestion scan, updates legacy history, and runs alert classification."""
    print(f"=== Initiating Ingestion Scan on System Target: {args.system} ===")
    
    # Decoupling Ingestion: Route to File Stream Parser if target file path provided
    if args.from_json and os.path.exists(args.from_json):
        print(f"[Ingestion] Parsing real external JSON log package stream: {args.from_json}")
        parser = JSONStreamParser()
        with open(args.from_json, "r") as f:
            metrics = parser.parse_string_payload(f.read())
    else:
        # Fall back to synthetic data streams
        if args.force_spike:
            hydrator = SyntheticHydrator(baseline_compute=450.0, baseline_memory=128.0)
        else:
            hydrator = SyntheticHydrator()
        metrics = hydrator.fetch_current_telemetry(args.system)
    
    # Historical Records: Retrieve past execution context paths from local storage disk
    logger = HistoricalRecordBuffer()
    window_history = logger.append_state(args.system, metrics.compute_cycles)
    
    detector = TelemetrySpikeDetector(deviation_threshold=1.8)
    
    # Safe slice passes history omitting the active iteration entry to avoid target echo bias
    historical_slice = window_history[:-1] if len(window_history) > 1 else []
    
    spike_result = detector.evaluate_window(
        system_id=args.system, metric_name="compute_cycles",
        current_value=metrics.compute_cycles, window_history=historical_slice
    )
    
    footprint = WebworkScore(
        system_integrity=4.2,
        operational_burnout=args.burnout,
        resource_overhead=1.5,
        knowledge_equity=4.0
    )
    
    classifier = AlertClassifier()
    alert = classifier.classify_event(spike_result, footprint)
    
    print(f"\n[Telemetry] CPU Cycles: {metrics.compute_cycles} | RAM: {metrics.memory_footprint}MB")
    print(f"[Historical Records] Sliding Window Active Count: {len(window_history)} frames")
    print(f"[Analysis]  Spike Verdict: {spike_result.verdict} (Variance Ratio: {spike_result.variance_ratio})")
    print(f"----------------------------------------------------------------------")
    print(f"[ALARM TRIGGER] Classification: {alert.classification}")
    print(f"[ALARM TRIGGER] Urgency Level:  {alert.urgency}")
    print(f"[ALARM TRIGGER] Action Summary: {alert.summary}")

def handle_tend(args) -> int:
    """Reports the Tending Ratio; returns non-zero only when --enforce is set and the ratio is below target."""
    broker = DebtBroker(repo_path=args.repo, required_ratio=args.ratio, window=args.window)
    stats = broker.parse_commit_stewardship()
    compliant = broker.verify_compliance(stats)
    mode = "ENFORCE" if args.enforce else "ADVISORY"

    print(f"=== Tending Ratio ({mode}) over last {stats['commits']} commits ===")
    print(f"Added: {stats['additions']} | Deleted: {stats['deletions']} (docs/tests excluded)")
    print(f"Ratio: {stats['tending_ratio']} | Target: {broker.required_ratio}")
    print("Result: " + ("meets target" if compliant else "below target - consider scheduling tending work"))

    return 1 if (args.enforce and not compliant) else 0

def main():
    parser = argparse.ArgumentParser(description="Reciprocal Operations (recip) CLI.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan_parser = subparsers.add_parser("scan", help="Run ingestion scans and classify alerts.")
    scan_parser.add_argument("--system", type=str, required=True, help="Target application system cluster ID.")
    scan_parser.add_argument("--burnout", type=float, default=2.0, help="Team-level load self-assessment (0-5). Aggregate and anonymous; never per person.")
    scan_parser.add_argument("--force-spike", action="store_true", help="Force a high-load time-series anomaly.")
    scan_parser.add_argument("--from-json", type=str, help="Optional external file path stream source destination.")

    tend_parser = subparsers.add_parser("tend", help="Report the Tending Ratio over recent commits.")
    tend_parser.add_argument("--repo", type=str, default=".", help="Path to the Git repository.")
    tend_parser.add_argument("--window", type=int, default=50, help="Number of recent commits to measure.")
    tend_parser.add_argument("--ratio", type=float, default=None, help="Target ratio (default: REQUIRED_TENDING_RATIO or 1.20).")
    tend_parser.add_argument("--enforce", action="store_true", help="Exit non-zero when below target (use in CI only with team agreement).")

    args = parser.parse_args()
    
    if args.command == "scan":
        handle_scan(args)
    elif args.command == "tend":
        sys.exit(handle_tend(args))

if __name__ == "__main__":
    main()
