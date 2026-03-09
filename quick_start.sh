#!/bin/bash

# Quick Start Script for AgriQuery AI
# This script automates the initial setup process

set -e  # Exit on error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Print functions
print_header() {
    echo -e "\n${BLUE}================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

# Check if Python 3 is installed
check_python() {
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | awk '{print $2}')
        print_success "Python $PYTHON_VERSION found"
        return 0
    else
        print_error "Python 3 is not installed"
        print_info "Please install Python 3.9 or higher from https://www.python.org/"
        exit 1
    fi
}

# Create virtual environment
create_venv() {
    print_info "Creating virtual environment..."

    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists"
        read -p "Do you want to recreate it? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            rm -rf venv
            python3 -m venv venv
            print_success "Virtual environment recreated"
        else
            print_info "Using existing virtual environment"
        fi
    else
        python3 -m venv venv
        print_success "Virtual environment created"
    fi
}

# Activate virtual environment
activate_venv() {
    print_info "Activating virtual environment..."

    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        print_success "Virtual environment activated"
    else
        print_error "Could not find venv/bin/activate"
        exit 1
    fi
}

# Install dependencies
install_dependencies() {
    print_info "Installing Python dependencies..."

    if [ -f "backend/requirements.txt" ]; then
        pip install --upgrade pip > /dev/null 2>&1
        pip install -r backend/requirements.txt
        print_success "Dependencies installed"
    else
        print_error "backend/requirements.txt not found"
        exit 1
    fi
}

# Run verification script
verify_setup() {
    print_info "Running setup verification..."

    if [ -f "setup_verify.py" ]; then
        python3 setup_verify.py
    else
        print_warning "setup_verify.py not found, skipping verification"
    fi
}

# Main setup function
main() {
    print_header "AgriQuery AI - Quick Start Setup"

    # Check if we're in the right directory
    if [ ! -f "README.md" ] || [ ! -d "backend" ]; then
        print_error "This script must be run from the AGRI-Query project root directory"
        exit 1
    fi

    print_info "This script will set up your development environment"
    echo

    # Step 1: Check Python
    print_header "Step 1: Checking Python Installation"
    check_python

    # Step 2: Create virtual environment
    print_header "Step 2: Setting Up Virtual Environment"
    create_venv

    # Step 3: Activate virtual environment
    print_header "Step 3: Activating Virtual Environment"
    activate_venv

    # Step 4: Install dependencies
    print_header "Step 4: Installing Dependencies"
    install_dependencies

    # Step 5: Verify setup
    print_header "Step 5: Verifying Setup"
    verify_setup

    # Final instructions
    print_header "Setup Complete! 🎉"
    echo
    print_success "Your development environment is ready!"
    echo
    print_info "Next steps:"
    echo "  1. Activate the virtual environment:"
    echo "     source venv/bin/activate"
    echo
    echo "  2. Start the backend server:"
    echo "     uvicorn backend.app:app --reload"
    echo
    echo "  3. Open the frontend:"
    echo "     Open frontend/index.html in your browser"
    echo
    echo "  4. Visit the API documentation:"
    echo "     http://localhost:8000/docs"
    echo
    echo "  5. Run the tests:"
    echo "     pytest tests/ -v"
    echo
    print_info "For more information, see CONTRIBUTING.md"
    echo
}

# Run main function
main
