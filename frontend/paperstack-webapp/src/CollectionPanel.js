import './CollectionPanel.css';

function CollectionPanel(props) {
  const items = props.collections.map(c => <li>{c.name}</li>);
  return (
    <div className="CollectionPanel">
      <h2>Panel</h2>
      <ul>{items}</ul>
    </div>
  );
}

export default CollectionPanel;

