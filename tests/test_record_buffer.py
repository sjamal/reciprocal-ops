"""
Unit verification suite verifying cyclical record window rotation and data preservation bounds.
"""

import os
from reciprocal_ops.storage.record_buffer import HistoricalRecordBuffer

def test_cyclical_record_truncation():
    test_log = "tests/test_history.json"
    logger = HistoricalRecordBuffer(file_path=test_log, max_window=3)
    
    # Append values past max threshold window parameters
    logger.append_state("cluster-x", 10.0)
    logger.append_state("cluster-x", 20.0)
    logger.append_state("cluster-x", 30.0)
    window = logger.append_state("cluster-x", 40.0)
    
    # Assert sliding limit strictly capped at maximum window width dimension
    assert len(window) == 3
    # 10.0 is cleanly dropped from the history loop, tracking elements 20, 30, and 40
    assert window == [20.0, 30.0, 40.0]
    
    if os.path.exists(test_log):
        os.remove(test_log)
