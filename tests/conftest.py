import sys
from pathlib import Path

# Add the workspace root to sys.path so that imports work correctly
workspace_root = Path(__file__).parent.parent
sys.path.insert(0, str(workspace_root))
