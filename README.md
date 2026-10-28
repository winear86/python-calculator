# Python Calculator

A clean, interactive command-line calculator built while learning Python.

This project demonstrates core programming concepts including classes, methods, error handling, input validation, and basic object-oriented design.

## Features

- Basic arithmetic operations (`+`, `-`, `*`, `/`, `**`, `%`)
- Support for parentheses
- Calculation history (last 10 results)
- Memory functions (`m+`, `m-`, `mr`, `mc`)
- Safe evaluation with clear error messages
- Graceful handling of invalid input and division by zero

## Skills Demonstrated

- Python classes and object-oriented programming
- Type hints
- Error handling with `try` / `except`
- Input validation
- Clean code structure and documentation
- Writing user-friendly command-line interfaces

## How to Run

1. Make sure you have Python 3.8+ installed
2. Clone the repository:
   ```bash
   git clone https://github.com/winear86/python-calculator.git
   cd python-calculator
   ```
3. Run the calculator:
   ```bash
   python3 calculator.py
   ```

## Example Usage

```
=== Python Calculator  (Learning Project) ===
Operations: +  -  *  /  **  %   (use parentheses)
Commands:
  history  → show recent calculations
  m+       → add last result to memory
  m-       → subtract last result from memory
  mr       → recall memory
  mc       → clear memory
  q / quit → exit
----------------------------------------
calc> 15 * 4 + 10
= 70.0

calc> (100 - 25) / 5
= 15.0

calc> 2 ** 10
= 1024

calc> m+
Added 1024.0 to memory. Memory = 1024.0

calc> history
--- History ---
15 * 4 + 10 = 70.0
(100 - 25) / 5 = 15.0
2 ** 10 = 1024
---------------

calc> q
Goodbye! Keep learning 🚀
```

## Future Improvements

- Add more scientific functions (sin, cos, sqrt, etc.)
- Support for variables
- Unit tests
- Graphical interface (Tkinter or web)

## License

This project is open source under the MIT License.

---

*Built as a learning project to practice Python fundamentals.*
