import unittest
from exemplo import demonstracao_git
from unittest.mock import patch

class TestDemonstracaoGit(unittest.TestCase):
    @patch('builtins.print')
    def test_demonstracao_output(self, mock_print):
        demonstracao_git()
        mock_print.assert_called()

if __name__ == '__main__':
    unittest.main()