import {useState, useEffect} from 'react';
import { Button, TextField } from '@mui/material';
import './QueryPanel.css';

const QLogic = {
  AND: 'AND',
  OR: 'OR'
}

const logics = [ QLogic.AND, QLogic.OR ];

const QOperator= {
  EQ: '==',
  NEQ: '!=',
  GT: '>',
  GEQ: '>=',
  LT: '<',
  LEQ: '<=',
  CONTAINS: 'CONTAINS',
}

class QCondition {
  constructor(name, key, operator, value) {
    this.name = name;
    this.key = key;
    this.operator = operator;
    this.value = value;
  }
}
class Query {
  constructor(logic, conditions) {
    this.logic = logic;
    this.conditions = conditions;
  }
}

const operators = [
  null,
  QOperator.EQ,
  QOperator.NEQ, 
  QOperator.GT,
  QOperator.GEQ,
  QOperator.LT,
  QOperator.LEQ,
  QOperator.CONTAINS,
];

const keys = [
  '', 'name', 'title', 'authors', 'tags', 'eprint', 'doi'
]

function queryStatement(logic, conditions) {
  var sql = 'SELECT * FROM document';
  if (logic !== null && conditions.length > 0) {
    sql += ' WHERE (';
    var op = null;
    if (logic === QLogic.AND || logic === QLogic.OR) {
      conditions.forEach(cond => {
        if (op !== null) sql += ' ' + op + ' ';
        const valueString = '"' + String(cond.value) + '"';
        sql += '(' + cond.key + ' ' + cond.operator + ' ' + valueString + ')';
        op = logic;
      });
      sql += ')';
    }
  }
  return sql;
}

function retrieveDocuments(logic, conditions) {
  const sql = queryStatement(logic, conditions);
  const docs = [
    {
    name: "document one",
    authors: ["T. Kono", "A. B"],
    title: 'The 1st document',
    docType: 'Article'
  },{
    name: "document two",
    authors: ["R. Back"],
    title: 'The 2nd document',
    docType: 'eprint'
  }
  ];
  console.log('Retrieve documents '+ docs.length + ', sql='+sql);
  return docs;
}

function QueryPanel({documentsRetrieved}) {
  const [logic, setLogic] = useState(QLogic.AND);
  const [conditions, setConditions] = useState([
    new QCondition('condition1', 'title', '!=', ''), 
    new QCondition('condition2', 'tags', 'contains', 'Meeting')
  ]);

  const logicItems = logics.map(x => (<option name={x} key={x}>{x}</option>));
  const keyItems = keys.map(key => <option name={key} key={key}>{key}</option>);
  const operatorItems = operators.map(x => 
    <option name={x} key={x}>{x}</option>
  )

  const conditionItems = conditions.map(c => <div className="ConditionItem" key={c.name}>
    <select>{keyItems}</select>
    <select>{operatorItems}</select>
    <input className="PropValue" type="text" defaultValue="none" />
  </div>);

  return (
    <div className="QueryPanel">
      <h2>Panel</h2>
      <div className="LogicRow">
        <label>Query: </label>
        <select onChange={e => setLogic(e)}>{logicItems}</select>
        <label> of the following conditions</label>
      </div>
      <div className="ConditionPanel">
        {conditionItems}
      </div>
      <Button variant="text" onClick={(e) => retrieveDocuments(logic, conditions)}>Retrieve</Button>
    </div>
  );
}

export default QueryPanel;
