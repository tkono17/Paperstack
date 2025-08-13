import React from 'react';
import './DocList.css';

function DocList(props) {
  const items = props.documents.map(x => <li>{x.name}</li>);

  return (
    <div className="DocList">
    <h2>Document list</h2>
    <ul>
    {items}
    </ul>
    </div>
  );
}

export default DocList;

