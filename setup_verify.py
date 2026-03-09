#!/usr/bin/env python3
"""
Setup Verification Script for AgriQuery AI

This script checks if your development environment is properly configured
and all dependencies are installed correctly.
"""

import sys
import os
import subprocess
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'


def print_header(text):
    """Print a styled header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'=' * 60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text:^60}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'=' * 60}{Colors.END}\n")


def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.END}")


def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.END}")


def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {text}{Colors.END}")


def print_info(text):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {text}{Colors.END}")


def check_python_version():
    """Check if Python version meets requirements"""
    print_info("Checking Python version...")
    version = sys.version_info
    version_str = f"{version.major}.{version.minor}.{version.micro}"

    if version.major == 3 and version.minor >= 9:
        print_success(f"Python {version_str} (meets requirement: 3.9+)")
        return True
    else:
        print_error(f"Python {version_str} (requires 3.9+)")
        print_warning("Please upgrade Python to version 3.9 or higher")
        return False


def check_virtual_environment():
    """Check if running inside a virtual environment"""
    print_info("Checking virtual environment...")

    in_venv = (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )

    if in_venv:
        print_success("Virtual environment is active")
        return True
    else:
        print_warning("Not running in a virtual environment")
        print_info("Recommendation: Activate venv with 'source venv/bin/activate'")
        return False


def check_project_structure():
    """Verify project directory structure"""
    print_info("Checking project structure...")

    required_dirs = ['backend', 'frontend', 'tests']
    required_files = [
        'backend/app.py',
        'backend/knowledge_graph.py',
        'backend/query_processor.py',
        'backend/graph_data.py',
        'backend/requirements.txt',
        'frontend/index.html',
        'frontend/style.css',
        'frontend/script.js',
        'tests/test_knowledge_graph.py',
        'tests/test_query_processor.py',
        'README.md'
    ]

    all_exist = True

    # Check directories
    for dir_name in required_dirs:
        if os.path.isdir(dir_name):
            print_success(f"Directory exists: {dir_name}/")
        else:
            print_error(f"Missing directory: {dir_name}/")
            all_exist = False

    # Check files
    for file_path in required_files:
        if os.path.isfile(file_path):
            print_success(f"File exists: {file_path}")
        else:
            print_error(f"Missing file: {file_path}")
            all_exist = False

    return all_exist


def check_dependencies():
    """Check if all required packages are installed"""
    print_info("Checking installed dependencies...")

    required_packages = {
        'fastapi': '0.100.0',
        'uvicorn': '0.23.0',
        'networkx': '3.1',
        'pydantic': '2.0.0',
        'pytest': '7.4.0',
        'httpx': '0.24.0'
    }

    all_installed = True

    for package, min_version in required_packages.items():
        try:
            # Try importing the package
            if package == 'uvicorn':
                import uvicorn
                version = uvicorn.__version__
            elif package == 'fastapi':
                import fastapi
                version = fastapi.__version__
            elif package == 'networkx':
                import networkx
                version = networkx.__version__
            elif package == 'pydantic':
                import pydantic
                version = pydantic.__version__
            elif package == 'pytest':
                import pytest
                version = pytest.__version__
            elif package == 'httpx':
                import httpx
                version = httpx.__version__

            print_success(f"{package} {version} installed")
        except ImportError:
            print_error(f"{package} not installed")
            all_installed = False

    if not all_installed:
        print_warning("Install missing packages with: pip install -r backend/requirements.txt")

    return all_installed


def check_backend_imports():
    """Check if backend modules can be imported"""
    print_info("Checking backend module imports...")

    modules_to_check = [
        'backend.app',
        'backend.knowledge_graph',
        'backend.query_processor',
        'backend.graph_data'
    ]

    all_imported = True

    for module_name in modules_to_check:
        try:
            __import__(module_name)
            print_success(f"{module_name} imports successfully")
        except Exception as e:
            print_error(f"{module_name} import failed: {str(e)}")
            all_imported = False

    return all_imported


def test_knowledge_graph():
    """Basic test of knowledge graph functionality"""
    print_info("Testing knowledge graph initialization...")

    try:
        from backend.graph_data import build_graph

        graph = build_graph()
        stats = graph.get_graph_stats()

        if stats['total_nodes'] > 0 and stats['total_edges'] > 0:
            print_success(f"Knowledge graph initialized: {stats['total_nodes']} entities, "
                         f"{stats['total_edges']} relationships")
            return True
        else:
            print_error("Knowledge graph is empty")
            return False
    except Exception as e:
        print_error(f"Knowledge graph test failed: {str(e)}")
        return False


def check_port_availability():
    """Check if default port 8000 is available"""
    print_info("Checking port availability...")

    import socket

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 8000))
    sock.close()

    if result != 0:
        print_success("Port 8000 is available")
        return True
    else:
        print_warning("Port 8000 is already in use")
        print_info("You can use a different port: uvicorn backend.app:app --port 8001")
        return True  # Not a critical failure


def print_summary(checks):
    """Print summary of all checks"""
    print_header("Setup Verification Summary")

    passed = sum(checks.values())
    total = len(checks)

    print(f"\nPassed: {passed}/{total} checks\n")

    for check_name, status in checks.items():
        if status:
            print_success(f"{check_name}")
        else:
            print_error(f"{check_name}")

    if passed == total:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 All checks passed! You're ready to start developing.{Colors.END}\n")
        print_info("Next steps:")
        print("  1. Start the backend: uvicorn backend.app:app --reload")
        print("  2. Open frontend/index.html in your browser")
        print("  3. Visit API docs: http://localhost:8000/docs")
        print("  4. Run tests: pytest tests/ -v")
        return True
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ Some checks failed. Please fix the issues above.{Colors.END}\n")
        print_info("Common fixes:")
        print("  • Activate virtual environment: source venv/bin/activate")
        print("  • Install dependencies: pip install -r backend/requirements.txt")
        print("  • Check you're in the project root directory")
        print("\n  For more help, see CONTRIBUTING.md")
        return False


def main():
    """Main verification function"""
    print_header("AgriQuery AI - Setup Verification")
    print_info("This script will verify your development environment setup\n")

    # Run all checks
    checks = {
        "Python version": check_python_version(),
        "Virtual environment": check_virtual_environment(),
        "Project structure": check_project_structure(),
        "Dependencies installed": check_dependencies(),
        "Backend imports": check_backend_imports(),
        "Knowledge graph": test_knowledge_graph(),
        "Port availability": check_port_availability()
    }

    # Print summary
    success = print_summary(checks)

    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
