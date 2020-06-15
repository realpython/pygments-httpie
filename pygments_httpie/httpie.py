"""Lexer for stdout from `httpie`.

Author: Brad Solomon <bsolomon@protonmail.com>
Taken heavily from httpie/output/formatters/colors.py.
"""

__all__ = ["HttpieLexer"]

import re

from pygments.lexer import RegexLexer, bygroups, using
from pygments.lexers.html import HtmlLexer
from pygments.lexers.shell import BashSessionLexer
from pygments.token import Keyword, Name, Number, Operator, String, Text


class HttpieLexer(RegexLexer):
    """Lexer for stdout from `httpie`."""

    name = "httpie"
    aliases = ["httpie"]
    flags = re.UNICODE | re.IGNORECASE

    tokens = {
        "root": [
            (r"^\$.*[\n\r]+", using(BashSessionLexer)),
            (
                r"([A-Z]+)( +)([^ ]+)( +)(HTTP)(/)(\d+\.\d+)",
                bygroups(
                    Name.Function,
                    Text,
                    Name.Namespace,
                    Text,
                    Keyword.Reserved,
                    Operator,
                    Number,
                ),
            ),
            (
                r"(HTTP)(/)(\d+\.\d+)( +)(\d{3})( +)(.+)",
                bygroups(
                    Keyword.Reserved,  # 'HTTP'
                    Operator,  # '/'
                    Number,  # Version
                    Text,
                    Number,  # Status code
                    Text,
                    Name.Exception,  # Reason
                ),
            ),
            (
                r"([-\w]+)( *)(:)( *)(.+)",
                bygroups(
                    Name.Attribute,  # Name
                    Text,
                    Operator,  # Colon
                    Text,
                    String,  # Value
                ),
            ),
            (
                r"(<!DOCTYPE)(\s+)([^>\s]+)([\[\]>])",
                bygroups(Keyword, Text, Name.Tag, Keyword),
            ),
            (r".*[\n\r]+", using(HtmlLexer)),
        ],
    }
