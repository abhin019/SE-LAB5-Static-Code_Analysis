# SE Lab 5 – Static Code Analysis

## Objective
Perform static code analysis using **Pylint**, **Bandit**, and **Flake8** to detect and fix code quality and security issues in `inventory_system.py`.

## Tools Used
- Pylint v3.x
- Bandit v1.8.6
- Flake8 v7.x

## Deliverables
- ✅ `inventory_system.py` – Cleaned and corrected code
- ✅ `reports/` – Folder containing analysis outputs:
  - `pylint_report.txt`
  - `bandit_report.txt`
  - `flake8_report.txt`
- ✅ `fixes_table.pdf` – Table listing all fixes applied
- ✅ `README.md` – Documentation and summary

## Results Summary
| Tool | Status | Remarks |
|------|---------|----------|
| Bandit | ✅ No medium/high issues | All security warnings resolved |
| Pylint | ✅ 9.47/10 | Style & logic improved |
| Flake8 | ✅ No issues | Formatting consistent |

## Author
Abhin – PES2UG23CS019


QUESTIONS:
Q1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest to fix were style-related issues like missing docstrings and snake_case naming, since they only required minor renaming or adding short comments.
The hardest was replacing eval() with ast.literal_eval, because it required understanding how to safely parse file input without executing arbitrary code.
Q2. Did the static analysis tools report any false positives? If so, describe one example.
No major false positives appeared. All flagged issues were valid. However, Pylint’s “global statement” warning was acceptable in this small script context.
Q3. How would you integrate static analysis tools into your workflow?
I would include Pylint, Flake8, and Bandit checks in a CI/CD pipeline (GitHub Actions) so that every commit is automatically scanned for code quality, style, and security issues. I’d also use pre-commit hooks locally to catch issues before pushing code.
Q4. What tangible improvements did you observe in the code quality after applying the fixes?
The code is now more readable, secure, and consistent. Files close automatically, functions are properly named, and unsafe practices like eval and bare exceptions are removed. The Pylint score increased from 4.8 to 9.75, reflecting major improvement in maintainability.
