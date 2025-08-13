import './DocProperties.css';

function valueField(name, value) {
  return (
    <div className="PropField">
    <label className="PropName">{name}</label>
    <input className="PropValue" type="text" id="{name}">{value}</input>
    </div>
  );
}

function listField(name, listValue) {
  const items = listValue.map(x => x + '\n');
  return (
    <div className="PropField">
    <label className="PropName">{name}</label>
    <textarea className="PropValue">{items}</textarea>
    </div>
  );
}

function propField(name, value) {
  var field = ''
  if (Array.isArray(value)) {
    field = valueField(name, value);
  } else if (typeof(value) in ["number", "string"]) {
    field = listField(name, value);
  } else {
    field = valueField(name, value);
  }
  return field;
}

function DocProperties(props) {
  const kvlist = [ ['name', props.name],
                   ['authors', props.authors],
                   ['title', props.title] ];
  const fields = kvlist.map(p => propField(p[0], p[1]));
    return (
      <div className="DocProperties">
      <h2>Document properties</h2>
      <ul>
      {fields}
      </ul>
      </div>
    );
}

export default DocProperties;
