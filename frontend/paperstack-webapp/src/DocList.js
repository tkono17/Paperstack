<<<<<<< HEAD
import React, {useState} from 'react';
import './DocList.css';

function DocList(props) {
  var [ lastQuery, setLastQuery] = useState('');
  var [ documents, setDocuments] = useState([]);

  documents = [ {
    name: "document one",
    authors: ["T. Kono", "A. B"],
    title: 'The 1st document',
    docType: 'Article'
  },{
    name: "document two",
    authors: ["R. Back"],
    title: 'The 2nd document',
    docType: 'eprint'
  }];

  /*if (props.queryName !== lastQuery) {
    console.log('Query updated to ' + props.queryName);
    setLastQuery(props.queryName);
    if (props.queryName === 'Collection A') {
      props.documentSelected(documents[0]);
    } else if (props.queryName === 'Collection B') {
      props.documentSelected(documents[1]);
    } else {
      props.documentSelected(null);
    }
  }*/

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

=======
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

>>>>>>> e77b56f8ec3a102cd20e7f214f11504fca852081
