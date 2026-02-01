import React, { useState } from 'react';
import {
    Box, Container, Stack,
    FormControl, Select, MenuItem,
    Tabs, Tab,
    Grid,
    Table, TableContainer,
    TableHead, TableBody, TableRow, TableCell,
    InputLabel, TextField, Typography,
    Icon
} from '@mui/material';
import ControlPointIcon from '@mui/icons-material/ControlPoint';
import './QueryList.css';
import QueryPanel from './QueryPanel';
import DocList from './DocList';

function QueryList(props) {
    const [value, setValue] = useState(1);
    const tabChanged = (event, newValue) => {
        console.log('New value: ', newValue);
        setValue(newValue);
    };

    return (<Stack backgroundColor="#a3adb8" padding={0.5} spacing={0.5}>
        <Box backgroundColor="#e6ede0" padding={1} borderRadius={1}>
            <Typography variant="h4">Server / Query</Typography>
            <Tabs className="ServerQueryTabs" value={value} onChange={tabChanged} lg={{ border: '1 solid grey' }}>
                <Tab label="Server" value={1} />
                <Tab label="Query" value={2} />
            </Tabs>
            <Box className="ServerQueryPanel" minHeight={100}>
                <Box value={value} index={1} hidden={value !== 1} padding={1}>
                    <TextField id="server-host" label="Server host: " variant="filled"></TextField>
                    <TextField id="server-port" label="Server port" variant="filled"></TextField>
                </Box>
                <Box value={value} index={2} hidden={value !== 2}>
                    <QueryPanel />
                </Box>

            </Box>
        </Box>
        <DocList />
    </Stack>);
}

export default QueryList;
