"""
Unit verification suite checking system record tracking and relational dependency data layers.
"""

import os
from reciprocal_ops.storage.record_registry import RecordRegistry, SystemProfile

def test_profile_registration_lifecycle():
    test_db = "tests/test_registry.json"
    registry = RecordRegistry(storage_path=test_db)
    
    profile = SystemProfile(
        system_id="api-gateway-node",
        historical_baseline_years=5,
        criticality_tier=1,
        legacy_dependencies_count=2,
        dependencies=["auth-service-pod", "backend-db-cluster"],
        operational_history_notes="Edge routing layer with mapped downstream cluster nodes."
    )
    
    registry.register_profile(profile)
    retrieved = registry.get_profile("api-gateway-node")
    
    assert retrieved is not None
    assert retrieved["dependencies"] == ["auth-service-pod", "backend-db-cluster"]
    assert retrieved["legacy_dependencies_count"] == 2
    
    if os.path.exists(test_db):
        os.remove(test_db)
