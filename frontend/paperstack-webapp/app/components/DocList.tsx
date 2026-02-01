import React, { useState } from 'react';
import {
  Typography,
  Box,
  TableContainer, Table, TableHead,
  TableRow, TableCell, TableBody,
  InputLabel
} from '@mui/material';
import './DocList.css';

function DocItemRow(props) {
  const doc = props.document;
  console.log('doc:', props.document);
  console.log('headers:', props.headers);
  return (
    <TableRow>
      <TableCell>
        <InputLabel>{doc.id}</InputLabel>
      </TableCell>
      <TableCell>
        <InputLabel>{doc.title}</InputLabel>
      </TableCell>
      <TableCell>
        <InputLabel>{doc.authors.join(', ')}</InputLabel>
      </TableCell>
      <TableCell>
        <InputLabel>{doc.docType}</InputLabel>
      </TableCell>
      <TableCell>
        <InputLabel>{doc.tags.join(', ')}</InputLabel>
      </TableCell>
    </TableRow>
  );
}

function DocList() {
  //{documents, documentSelected}
  const headers = [
    'id', 'title', 'authors', 'document type', 'tags'
  ]
  const documents = [
    {
      'id': 1,
      'title': 'Document A',
      'authors': ['T. Kono'],
      'docType': 'Article',
      'tags': ['Tag1',]
    },
    {
      'id': 2,
      'title': 'Document B',
      'authors': ['T. Kono', 'Someone else'],
      'docType': ['Book'],
      'tags': ['Tag2', 'Tag3']
    }
  ]
  return (
    <Box backgroundColor="#dcd8e1" padding={1} borderRadius={1}>
      <Typography variant="h4">List</Typography>
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              {headers.map((x) =>
                <TableCell>
                  <InputLabel>{x}</InputLabel>
                </TableCell>
              )}
            </TableRow>
          </TableHead>
          <TableBody>
            {documents.map((x) => (
              <DocItemRow headers={headers} document={x} />))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  );
}

export default DocList;

