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
