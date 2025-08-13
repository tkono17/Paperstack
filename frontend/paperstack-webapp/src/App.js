//import logo from './logo.svg';
import './App.css';
import CollectionPanel from './CollectionPanel.js';
import DocList from './DocList.js';
import DocProperties from './DocProperties.js';

function App() {
  const collections = [
    {
      name: "Collection A",
      condition: "name != \"\""
    },{
      name: "Collection B",
      condition: "name != \"\""
    }
  ];
  const documents = [
    {
      name: "Document 1",
      authors: [ "A. Back", "C. Dixon" ],
      title:"Title 1",
      docType: "Article"
    },{
      name:"Document 2",
      authors:[ "A. Back", "C. Dixon" ],
      title:"Title 2",
      docType: "Manual"
    }
  ];

  return (
    <div className="App">
    <CollectionPanel collections={collections} />
    <DocList documents={documents} />
    <DocProperties document={document[0]} />
    </div>
  );
  /* return (
   *   <div className="App">
   *     <header className="App-header">
   *       <img src={logo} className="App-logo" alt="logo" />
   *       <p>
   *         Edit <code>src/App.js</code> and save to reload.
   *       </p>
   *       <a
   *         className="App-link"
   *         href="https://reactjs.org"
   *         target="_blank"
   *         rel="noopener noreferrer"
   *       >
   *         Learn React
   *       </a>
   *     </header>
   *   </div>
   * ); */
}

export default App;
