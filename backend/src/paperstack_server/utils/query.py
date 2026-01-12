from enum import Enum
from dataclasses import dataclass

class QueryOperator(Enum):
    EQ = '=='
    NEQ = '!='
    GT = '>'
    GE = '>='
    LT = '<'
    LE = '<='
    CONTAINS = 'CONTAINS'
    
QOp = QueryOperator

class QueryLogic(Enum):
    AND = '&'
    OR = '|'
    NOT = '!'

QL = QueryLogic

@dataclass
class QueryCondition:
    name: str
    id: int

    def passed(self, data):
        x = False
        return x

@dataclass
class SimpleQCondition(QueryCondition):
    op: QueryOperator
    fieldName: str
    value: int | float | str

    def passed(self, data):
        x = False
        actualValue = None
        if self.fieldName in data:
            actualValue = data[self.fieldName]
        else:
            return x
        match self.op:
            case QOp.EQ: x = actualValue == self.value
            case QOp.NEQ: x = actualValue != self.value
            case QOp.GT: x = actualValue > self.value
            case QOp.GE: x = actualValue >= self.value
            case QOp.LT: x = actualValue < self.value
            case QOp.LE: x = actualValue <= self.value
            case QOp.CONTAINS:
                x = actualValue.lower().contains(self.value.lower())>=0
        return x

@dataclass
class CompositeQCondition(QueryCondition):
    logic: QueryLogic
    conditions: list[QueryCondition]

    def passed(self, data):
        y = False
        results = [ cond.passed(data) for cond in self.conditions ]
        n = len(conditions)
        match self.logic:
            case QL.NOT:
                if n==1: y = not results[0]
            case QL.AND:
                if results.count(True)==n: y = True
            case QL.NOT:
                if results.count(True)>0: y = True
        return y
    

class QCgen:
    @classmethod
    def condition(name, key, op, value):
        return SimpleQCondition(name, key, op, value)
        
    @classmethod
    def composite(name, logic, conditions):
        return CompositeQCondition(name, logic, conditions)

    @classmethod
    def Not(name, conditions):
        return self.composite(name, QL.NOT, conditions)
        
    @classmethod
    def And(name, conditions):
        return self.composite(name, QL.AND, conditions)
        
    @classmethod
    def Or(name, conditions):
        return self.composite(name, QL.OR, conditions)
        
        
#
# Condition('name', QOp.CONTAINS, 'part')
# AND([1, 2, 3])
# NOT(1)
# 
