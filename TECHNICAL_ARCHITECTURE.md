# Technical Architecture - NPC Therapy Game

## Overview

The NPC Therapy Game is a complete web application with integrated API functionality, character database management, and full-stack deployment capabilities.

## Technical Stack

### Frontend
- **HTML5/CSS3/JavaScript**: Core game interface
- **Multiple Game Variants**: 12+ HTML versions with progressive enhancement
- **Responsive Design**: Mobile and desktop compatible
- **Image Optimization**: 60+ character images with metadata tracking

### Backend & API
- **Node.js/Express**: HTTP server for API endpoints
- **External API Integration**: Data sources for enhanced functionality
- **Static File Serving**: Optimized asset delivery
- **Health Monitoring**: API health checks and logging

### Data Management
- **Character Database**: 40+ NPCs with detailed therapy scripts
- **Image Metadata**: AI-generated quality scores and descriptions
- **Batch Processing**: Organized character scripts across 10 batch files
- **Cross-Reference System**: Character relationships and meta-narratives

## API Endpoints

### Core Endpoints
```
GET /                    → Serve main game (index.html)
GET /api/health          → Health check and server status
GET /api/characters      → Character database access
GET /imgs/*              → Serve character images
```

### Character API Structure
```json
{
  "character": {
    "name": "Character Name",
    "backstory": "Detailed background",
    "therapy_session": "Therapy dialogue",
    "symbolic_items": "Important objects",
    "cross_references": "Related characters",
    "meta_moments": "Meta-narrative elements"
  }
}
```

## File Structure

```
npc-therapy-game/
├── index.html                           # Main game file
├── server.js                           # Express.js server
├── package.json                        # Node.js configuration
├── DEPLOY.md                          # Deployment instructions
├── image_meta.json                    # Image metadata (912 entries)
├── external_api/                      # API integration layer
│   ├── __init__.py
│   ├── function_utils.py
│   ├── mcp_function_list.json
│   └── data_sources/                  # Data integration
│       ├── base.py
│       ├── booking_source.py
│       ├── yahoo_source.py
│       └── [7 other data sources]
├── characters/                        # Character database
│   ├── CHARACTER_INDEX.md            # Complete character directory
│   └── batches/                      # 10 batch files with NPC scripts
├── imgs/                             # Visual assets
│   ├── therapy_office.png           # Main background
│   ├── character_habitats/          # 30+ habitat images
│   └── therapy_office/              # 30+ therapy session portraits
└── docs/                            # Complete documentation
    ├── GAME_SUMMARY.md
    ├── ENHANCED_FEATURES_GUIDE.md
    ├── ULTIMATE_IMPLEMENTATION_GUIDE.md
    └── [5 additional documentation files]
```

## API Integration Details

### External Data Sources
The `external_api/data_sources/` directory contains integration modules for:
- **Booking**: Travel and accommodation data
- **Yahoo Finance**: Financial market data
- **Twitter**: Social media insights
- **Pinterest**: Visual content discovery
- **Patent**: Patent search capabilities
- **Scholar**: Academic research
- **Commodities/Metal**: Market pricing
- **TripAdvisor**: Location and travel data

### Image Processing Pipeline
1. **Generation**: AI-generated character sprites with specific prompts
2. **Metadata**: Quality scores, dimensions, format analysis
3. **Storage**: Organized in habitat and therapy office categories
4. **API Integration**: Dynamic loading and display in game interface

## Deployment Options

### Local Development
```bash
npm install
npm start
# Server runs on http://localhost:3000
```

### GitHub Pages
- Repository: https://github.com/12Matt3r/Npctherapy
- Static files automatically served
- Enable GitHub Pages for live deployment

### Production Deployment
1. **Node.js Hosting**: Heroku, Railway, DigitalOcean
2. **Static Hosting**: Netlify, Vercel
3. **Docker**: Containerized deployment available

## Configuration Files

### package.json
- Node.js dependencies and scripts
- Metadata for package management
- Repository and homepage links

### image_meta.json
- 912 entries of image metadata
- AI-generated quality scores
- Prompt-response correlation data
- Technical specifications (dimensions, format, size)

### external_api/
- Modular API integration
- Configuration for external services
- Rate limiting and error handling

## Security & Performance

### Security Features
- Input validation on API endpoints
- CORS configuration for cross-origin requests
- Error handling middleware
- Static file serving with proper headers

### Performance Optimizations
- Static asset caching
- Compressed image delivery
- Minimal dependencies
- Optimized JavaScript loading

## Development Notes

### Character Database Integration
- Character scripts stored in Markdown format
- Batch processing for efficient loading
- Cross-reference system for meta-narratives
- Dynamic therapy session generation

### Image Asset Management
- Organized by usage context (habitat vs therapy office)
- AI-generated with quality scoring
- Metadata tracking for optimization
- Responsive image delivery

### API Design Patterns
- RESTful endpoint structure
- JSON response formatting
- Error handling and logging
- Health monitoring integration

## Future Enhancements

### Planned Features
- Real-time therapy session logging
- Character progression tracking
- Enhanced meta-narrative elements
- Multiplayer therapy sessions
- Advanced AI integration for dynamic responses

### Technical Roadmap
- Database integration (PostgreSQL/MongoDB)
- User authentication and progress saving
- Enhanced API rate limiting
- Advanced caching strategies
- Mobile app development

---

*Last Updated: 2025-11-01*  
*Version: 1.0.0*  
*Repository: https://github.com/12Matt3r/Npctherapy*