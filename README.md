# ♟️ Chess Tournament Manager ♟️

Python application for managing chess tournaments using the Swiss pairing system. Built with MVC architecture and featuring a terminal interface by Rich.

### 👥 Player Management
- ✅ Add new players with validation (name, surname, birthday, national ID)
- ✅ Modify existing player information
- ✅ View all registered players in alphabetical order

### 🏆 Tournament Management
- ✅ Create tournaments with customizable number of rounds
- ✅ Register/unregister players (only during registration phase)
- ✅ Launch tournaments with automatic rounds generation
- ✅ Three tournament statuses: **Registration**, **In progress**, **Done**
- ✅ Delete tournaments, only when status is in "registration" state
- ✅ Minimum player requirement calculated based on the number of rounds

### ⚔️ Match Management
- ✅ **Swiss pairing system** implementation
  - Round 1: Random shuffle
  - Other rounds: Score based pairing
  - Automatic rematch avoidance when possible
- ✅ Enter each match results for the round (Win: 1pt, Draw: 0.5pt, Loss: 0pt)
- ✅ Launch next round when match results fully completed
- ✅ Real-time score tracking

### 📊 Reports
- ✅ View all tournaments with status indicators
- ✅ Detailed tournament reports showing:
  - All rounds with match results
  - Visual indicators (✅ Win, ❌ Loss, 🤝 Draw)
  - Final standings with podium (🥇🥈🥉)
  - Displaying tournament winner(s)
- ✅ Support for tie scenarios

### 🎨 User Interface
- ✅ Terminal UI with Rich library
- ✅ Color-coded status indicators
- ✅ Intuitive navigation
- ✅ Form validation with clear error messages
- ✅ Cancel operations with "0" input


### Prerequisites needed for using the application
Follow these steps :
- Recreate the virtual environment
- Activate the virtual environment
- Install the dependencies : `pip install -r requirements.txt`
- Run the application : `python main.py`

If you need to generate a new flake 8 rapport :
- Delete the old flake8 rapport file
- Create the new one : `flake8 --format=html --htmldir=flake8_rapport`