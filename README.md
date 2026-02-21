# py-mini-project

## Overview
A minimal Flask project for reacclimating with Python and Flask. Provides time utilities and math operations via API endpoints.

## Setup
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the app:
   ```
   python run.py
   ```

## API Endpoints
- `/current-time`: Get current timestamp.
- `/current-time-inverted`: Get current timestamp in inverted format.
- `/calculate?a=<num>&b=<num>`: Divide `a` by `b` and get result with timestamp.
- `/reports-stats`: Get count of successful calculation reports.

## Testing
Run tests with pytest.

## Notes
- Uses Singleton pattern for managers.
- All responses are JSON.
