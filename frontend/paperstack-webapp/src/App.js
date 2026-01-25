//import logo from './logo.svg';
import {useState} from 'react';
import { Container, Grid, CssBaseline, Box, Typography } from '@mui/material'
import './App.css';
import QueryList from './QueryList.js';
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
    <Container maxWidth="lg" justifyContents="center">
      <CssBaseline />
      <Typography  fullWidth={true} variant="h2" color="#125644" backgroundColor="#88cc88">Paperstack</Typography>
      <Grid container>
        <Grid size={7}>
          <QueryList />
        </Grid>
        <Grid size={5}>
          <DocProperties document={currentDoc} />
        </Grid>
      </Grid>
    </Container>
  );

}

export default App;
