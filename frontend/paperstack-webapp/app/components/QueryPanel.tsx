import React, { useState } from 'react';
import {
    Box, Container, Stack,
    FormControl, Select, MenuItem, IconButton,
    Tabs, Tab,
    Grid,
    Table, TableContainer,
    TableHead, TableBody, TableRow, TableCell,
    InputLabel, TextField, Typography,
    Icon
} from '@mui/material';
import ControlPointIcon from '@mui/icons-material/ControlPoint';
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

function QueryPanel() {
    return (
        <Stack>
            <FormControl style={{ width: "50%" }}>
                <InputLabel id="query-label">Query</InputLabel>
                <Select labelId="query-label" id="query" label="Query">
                    <MenuItem>Articles</MenuItem>
                    <MenuItem>Datasheet</MenuItem>
                </Select>
            </FormControl>
            <Grid container justify-content="center" alignItems="center">
                <Grid size={2} >
                    <IconButton fullWidth disabled><RemoveCircleOutlineIcon /></IconButton>
                    <IconButton fullWidth><ControlPointIcon /></IconButton>
                </Grid>
                <Grid size={3}>
                    <TextField label="Field name" variant="filled"></TextField>
                </Grid>
                <Grid size={2}>
                    <FormControl fullWidth>
                        <InputLabel id="query-operator-label">Query</InputLabel>
                        <Select labelId="query-operator-label" id="query-operator" label="Operator">
                            <MenuItem>==</MenuItem>
                            <MenuItem>!=</MenuItem>
                            <MenuItem>&lt</MenuItem>
                            <MenuItem>&lt=</MenuItem>
                            <MenuItem>&gt</MenuItem>
                            <MenuItem>&ge</MenuItem>
                            <MenuItem>contains</MenuItem>
                        </Select>
                    </FormControl>
                </Grid>
                <Grid size={4}>
                    <TextField label="Field value" variant="filled"></TextField>
                </Grid>
            </Grid>
        </Stack>);
}

export default QueryPanel;