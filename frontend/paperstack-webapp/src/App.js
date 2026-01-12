<<<<<<< HEAD
//import logo from './logo.svg';
import {useState} from 'react';
import './App.css';
import CollectionPanel from './CollectionPanel.js';
import DocList from './DocList.js';
import DocProperties from './DocProperties.js';

function App() {
  const [collection, setCollection] = useState('');
  const [currentDoc, setCurrentDoc] = useState(null);

  const collectionSelected = (c) => {
    collection = setCollection(c);
  };

  const documentSelected = function(x) {
    console.log('Document selected: ' + x)
    setCurrentDoc(x);
  }

  return (
    <div className="App">
    <CollectionPanel collectionSelected={(x) => setCollection(x)}/>
    <DocList queryName={collection} documentSelected={documentSelected} />
    <DocProperties document={currentDoc} />
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
=======
//import logo from './logo.svg';
import {useState} from 'react';
import './App.css';
import QueryPanel from './QueryPanel.js';
import DocList from './DocList.js';
import DocProperties from './DocProperties.js';


function App() {
  const [documents, setDocuments] = useState([]);
  const [currentDoc, setCurrentDoc] = useState({
    name: "document one",
    authors: ["T. Kono", "A. B"],
    title: 'The 1st document',
    docType: 'Article'
  });

  return (
    <div className="App">
    <QueryPanel documentsRetrieved={(x) => setDocuments(x)}/>
    <DocList documents={documents} documentSelected={(x) => setCurrentDoc(x)} />
    <DocProperties document={currentDoc} />
    </div>
  );

}

export default App;
>>>>>>> e77b56f8ec3a102cd20e7f214f11504fca852081
