import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class TradingTests(unittest.TestCase):
    def test_paper_buy_sell(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "main.py")],
            input="buy\n2\nsell\n1\nquit\n",
            text=True, capture_output=True, timeout=10,
            cwd=ROOT
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("PAPER TRADING ONLY", result.stdout)
        self.assertIn("Shares: 1", result.stdout)
