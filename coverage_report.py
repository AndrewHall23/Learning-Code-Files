import json
from datetime import datetime

def print_coverage_report(coverage_file='coverage.json'):
    """Parse and display coverage.json in a human-readable format"""
    
    with open(coverage_file, 'r') as f:
        data = json.load(f)
    
    meta = data['meta']
    totals = data['totals']
    files = data['files']
    
    # Header
    print("\n" + "="*80)
    print("TEST COVERAGE REPORT".center(80))
    print("="*80)
    print(f"Coverage Version: {meta['version']}")
    print(f"Generated: {meta['timestamp']}")
    print(f"Branch Coverage: {'Yes' if meta['branch_coverage'] else 'No'}")
    print("="*80 + "\n")
    
    # Overall Summary
    print("OVERALL SUMMARY")
    print("-" * 80)
    print(f"  Total Statements:        {totals['num_statements']}")
    print(f"  Covered Lines:           {totals['covered_lines']}")
    print(f"  Missing Lines:           {totals['missing_lines']}")
    print(f"  Coverage Percentage:     {totals['percent_covered_display']}% ({totals['percent_covered']:.2f}%)")
    print("-" * 80 + "\n")
    
    # File Breakdown
    print("FILE BREAKDOWN")
    print("-" * 80)
    for file_name, file_data in files.items():
        summary = file_data['summary']
        print(f"\nFile: {file_name}")
        print(f"  Covered Lines:     {summary['covered_lines']}/{summary['num_statements']}")
        print(f"  Coverage:          {summary['percent_covered_display']}% ({summary['percent_covered']:.2f}%)")
        
        if file_data['missing_lines']:
            print(f"  Missing Lines:     {', '.join(map(str, file_data['missing_lines']))}")
    
    print("\n" + "-" * 80)
    
    # Test Class Summary
    if 'functions' in files.get(list(files.keys())[0], {}):
        print("\nTEST CLASS BREAKDOWN")
        print("-" * 80)
        
        test_file = files['test_calculator.py']
        classes = test_file.get('classes', {})
        
        for class_name, class_data in classes.items():
            if class_name == "":  # Skip module-level
                continue
            summary = class_data['summary']
            print(f"\n{class_name}")
            print(f"  Covered Lines:     {summary['covered_lines']}/{summary['num_statements']}")
            print(f"  Coverage:          {summary['percent_covered_display']}%")
    
    print("\n" + "="*80 + "\n")

if __name__ == '__main__':
    print_coverage_report()
