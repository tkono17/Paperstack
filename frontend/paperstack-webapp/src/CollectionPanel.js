import './CollectionPanel.css';

function CollectionPanel(props) {
  const collections = [
    {
      name: "Collection A",
      condition: "name != \"\""
    },{
      name: "Collection B",
      condition: "name != \"\""
    }
  ];

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
