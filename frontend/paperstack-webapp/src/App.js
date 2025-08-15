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
