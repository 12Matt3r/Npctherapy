#!/usr/bin/env node

/**
 * NPC Therapy Game - Server Configuration
 * Handles serving static files and API endpoints
 */

const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3000;

// Serve static files from 'imgs' directory
app.use('/imgs', express.static(path.join(__dirname, 'imgs')));

// Serve static files from root directory
app.use(express.static(__dirname));

// API endpoint to get character data
app.get('/api/characters', (req, res) => {
    try {
        // This would integrate with your character database
        res.json({
            success: true,
            message: 'Character API endpoint ready for integration',
            characters: 'Loaded from /characters/batches/ directory'
        });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.json({
        status: 'healthy',
        timestamp: new Date().toISOString(),
        version: '1.0.0',
        game: 'NPC Therapy Game'
    });
});

// Serve main game file
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Create logs directory if it doesn't exist
const logsDir = path.join(__dirname, 'logs');
if (!fs.existsSync(logsDir)) {
    fs.mkdirSync(logsDir);
}

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
});

app.listen(PORT, () => {
    console.log(`
    🎮 NPC Therapy Game Server
    =====================================
    🌐 Server running on port ${PORT}
    🎭 Game available at: http://localhost:${PORT}
    📊 Health check: http://localhost:${PORT}/api/health
    🤖 Characters API: http://localhost:${PORT}/api/characters
    =====================================
    `);
});

module.exports = app;