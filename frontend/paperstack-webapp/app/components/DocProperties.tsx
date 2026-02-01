import React from 'react';
import {
  TextField, InputLabel, Typography,
  Grid, Container
} from '@mui/material';
import './DocProperties.css';

function valueField(name : string, value : string | number) {
  const vname = 'value-' + name;
  let vfield;
  console.log('name = ' + name);
  if (name === 'authors: ') {
    console.log(' is authors')
    vfield = <textarea className="PropValue" type="text" key={vname}
      onKeyUp={(event) => {
//        const padding = 0;
//        event.target.style.height = "inherit";
//        console.log('Text area changed, height=' + String(event.target.scrollHeight));
//        event.target.style.height = (event.target.scrollHeight - padding) + 'px';
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
  var field = valueField(name, value);
  return field;
}

function DocProperties({ document }) {
  console.log('Document updated...' + document);
  var kvlist : string[][] = [];
  if (document === null) {
    kvlist = [];
  } else {
    document.authors = 'A. Back\nC. Dag\nN. Leick';
    kvlist = [['name', document.name],
    ['authors', document.authors],
    ['title', document.title]
    ];
  }
  var fields = kvlist.map(p => propField(p[0] + ': ', p[1]));

  const keys = [
    'id', 'title', 'authors', 'document type', 'tags',
    'eprint', 'url', 'doi', 'reference'
  ]
  return (
    <Container>
      <Typography variant="h4">Document</Typography>
      <Grid container justify-content="center" alignItems="center">
        {keys.map(key => (
          <>
            <Grid align="left" size={4}>
              <InputLabel>{key}</InputLabel>
            </Grid>
            <Grid size={8}>
              <TextField label={key}></TextField>
            </Grid>
          </>))}
      </Grid>
    </Container>
  );
}

export default DocProperties;
