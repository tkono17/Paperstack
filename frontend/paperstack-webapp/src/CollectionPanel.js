import {useState, useEffect} from 'react';
import './CollectionPanel.css';

function CollectionPanel(props) {
  const [collections, setCollections] = useState([{
    'name': 'Articles',
    'op': '==',
    'fieldName': 'docType',
    'value': 'Article'
  }]);

  useEffect(() => {
    fetch('http://localhost:3100/query/', {method: 'GET', mode: 'cors'})
    .then(res => res.json())
    .then(data => {
      setCollections(data);
      console.log('Fetched data');
  })
    .catch(error => console.log(error))
  }, []);


  const items = collections.map(c => <option value={c.name} key={c.name}>{c.name}</option>);

  return (
    <div className="CollectionPanel">
      <h2>Panel</h2>
      <select onChange={(e) => props.collectionSelected(e.target.value)}>
        {items}
      </select>
    </div>
  );
}

export default CollectionPanel;
