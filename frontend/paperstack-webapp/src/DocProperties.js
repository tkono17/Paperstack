import './DocProperties.css';

function valueField(name, value) {
  return (
    <div className="PropField" key={name}>
    <label className="PropName" for={name}>{name}</label>
    <input className="PropValue" type="text" name={name} value={value} />
    </div>
  );
}

function listUpdated(text) {
  console.log('List updated:' + text)
}

function listField(name, listValue) {
  const n = listValue.length;
  const items = listValue.toString().replace(',', '\n');
  console.log('List values: ' + items);
  return (
    <div className="PropField" key={name}>
    <label className="PropName">{name}</label>
    <textarea className="PropValue" rows={n} value={items} onChange={listUpdated}></textarea>
    </div>
  );
}

function propField(name, value) {
  var field = ''
  if (Array.isArray(value)) {
    field = listField(name, value);
  } else if (typeof(value) in ["number", "string"]) {
    field = valueField(name, value);
  } else {
    field = valueField(name, value);
  }
  return field;
}

function DocProperties(props) {
  console.log('Document updated...' + props.document);
  var kvlist = [];
  if (props.document === null) {
    kvlist = [];
  } else {
    kvlist = [ ['name', props.document.name],
    ['authors', props.document.authors],
    ['title', props.document.title]
  ];
  }
  var fields = kvlist.map(p => propField(p[0]+': ', p[1]));
  console.log('N fields: ' + fields.length + ' ' + fields);
  return (
    <div className="DocPropertiesPanel">
      <h2>Document properties</h2>
      <div className="DocProperties">
      {fields}
      </div>
    </div>
  );
}

export default DocProperties;
