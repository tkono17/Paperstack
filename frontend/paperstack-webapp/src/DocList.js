import React, {useState} from 'react';
import './DocList.css';

function DocList({documents, documentSelected}) {

  const items = documents.map(x => 
    <div className="DocItem" key={x.name}>
      <div className="row1" key="1">{x.name} ({x.docType})</div>
      <div className="row2" key="2">{x.authors}</div>
      <div className="row3" key="3">{x.title}</div>
    </div>);

  return (
    <div className="DocListPanel">
      <h2>Document list</h2>
      <div className="DocList">
        {items}
      </div>
    </div>
  );
}

export default DocList;

