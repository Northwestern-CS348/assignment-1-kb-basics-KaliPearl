import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact: object) -> object:
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        if not isinstance(fact, Fact):
            print('kb_assert: not a fact')
            return
        if fact in self.facts:
            print('kb_assert: fact already present')
            return
        self.facts.append(fact)

        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))

        output = ListOfBindings ()
        for x in self.facts:
            found = match(x.statement, fact.statement,)
            if found:
                output.add_bindings(found)
                """do I need fact input here- try without"""
        if not output:
            return False
        return output
