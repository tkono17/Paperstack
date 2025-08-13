import React from 'react';
import './DocList.css';

function DocList(props) {
  const items = props.documents.map(x => <li className="DocItem">
    <div className="row1">{x.name} ({x.docType})</div>
    <div className="row2">{x.authors}</div>
    <div className="row3">{x.title}</div>
    </li>);

  return (
    <div className="DocListPanel">
    <h2>Document list</h2>
    <ul className="DocList">
    {items}
    </ul>
    </div>
  );
}

export default DocList;

