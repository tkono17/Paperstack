<<<<<<< HEAD
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
=======
import React from 'react';
import { TextField } from '@mui/material';
import './DocProperties.css';

function valueField(name, value) {
  const vname = 'value-'+name;
  let vfield;
  console.log('name = ' + name);
  if (name === 'authors: ') {
    console.log(' is authors')
    vfield = <textarea className="PropValue" type="text" key={vname} 
      onKeyUp={ (event) => {
        const padding = 0;
        event.target.style.height = "inherit";
        console.log('Text area changed, height=' + String(event.target.scrollHeight));
        event.target.style.height = (event.target.scrollHeight-padding)+'px';
      }} defaultValue={value} />; 
  } else {
    console.log('  others');
    vfield = <input className="PropValue" type="text" key={vname} defaultValue={value} />;
  }

  return (
    <React.Fragment>
    <label className="PropName" key={name}>{name}</label>
    {vfield}
    </React.Fragment>
  );
}

function listUpdated(text) {
  console.log('List updated:' + text)
}

function propField(name, value) {
  var field = ''
  field = valueField(name, value);
  return field;
}

function DocProperties({document}) {
  console.log('Document updated...' + document);
  var kvlist = [];
  if (document === null) {
    kvlist = [];
  } else {
    document.authors = 'A. Back\nC. Dag\nN. Leick';
    kvlist = [ ['name', document.name],
    ['authors', document.authors],
    ['title', document.title]
  ];
  }
  var fields = kvlist.map(p => propField(p[0]+': ', p[1]));

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
>>>>>>> e77b56f8ec3a102cd20e7f214f11504fca852081
