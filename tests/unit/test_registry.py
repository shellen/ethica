# ABOUTME: Unit tests for framework registry
# ABOUTME: Tests framework loading, listing, and validation

"""
Tests for framework registry.
"""

import pytest
from pathlib import Path

from ethica.core.registry import FrameworkRegistry


def test_list_frameworks():
    """Test listing available frameworks"""
    registry = FrameworkRegistry()
    frameworks = registry.list_frameworks()

    assert len(frameworks) > 0
    assert any(fw["id"] == "unesco-2021" for fw in frameworks)


def test_get_framework():
    """Test getting framework metadata"""
    registry = FrameworkRegistry()
    framework = registry.get_framework("unesco-2021")

    assert framework is not None
    assert framework["id"] == "unesco-2021"
    assert framework["name"] == "UNESCO AI Ethics Recommendation 2021"
    assert "category" in framework


def test_get_nonexistent_framework():
    """Test getting a framework that doesn't exist"""
    registry = FrameworkRegistry()
    framework = registry.get_framework("nonexistent")

    assert framework is None


def test_load_framework_spec():
    """Test loading complete framework specification"""
    registry = FrameworkRegistry()
    spec = registry.load_framework_spec("unesco-2021")

    assert spec is not None
    assert "metadata" in spec
    assert "principles" in spec
    assert "checks" in spec
    assert spec["metadata"]["id"] == "unesco-2021"


def test_load_nonexistent_framework_spec():
    """Test loading spec for nonexistent framework"""
    registry = FrameworkRegistry()

    with pytest.raises(ValueError, match="not found in registry"):
        registry.load_framework_spec("nonexistent")


def test_framework_spec_structure():
    """Test that framework spec has required structure"""
    registry = FrameworkRegistry()
    spec = registry.load_framework_spec("unesco-2021")

    # Check metadata
    assert "id" in spec["metadata"]
    assert "name" in spec["metadata"]
    assert "version" in spec["metadata"]

    # Check principles
    assert len(spec["principles"]) > 0
    for principle in spec["principles"]:
        assert "id" in principle
        assert "name" in principle
        assert "weight" in principle

    # Check checks
    assert len(spec["checks"]) > 0
    for check in spec["checks"]:
        assert "id" in check
        assert "name" in check
        assert "type" in check
        assert "severity" in check
        assert "principle" in check
