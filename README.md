# Genomic Insights Dashboard

<div align="center">

**A sophisticated bioinformatics platform for personalized genetic analysis**

[![Technology](https://img.shields.io/badge/Bioinformatics-Computational_Biology-4A90E2?style=for-the-badge)](https://github.com)
[![React](https://img.shields.io/badge/React-18.2.0-61DAFB?style=for-the-badge&logo=react&logoColor=white)](https://reactjs.org)
[![Flask](https://img.shields.io/badge/Flask-2.3.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

[Features](#features) • [Installation](#installation) • [Documentation](#documentation) • [Research](#genetic-markers) • [Contributing](#contributing)

</div>

---

## Overview

Genomic Insights Dashboard is a full-stack web application that transforms raw genetic data into actionable insights. Built for researchers, educators, and bioinformatics enthusiasts, this platform analyzes 23andMe-formatted genomic files to reveal patterns in athletic performance, physical traits, health predispositions, and metabolic characteristics.

### Key Capabilities

- **Comprehensive Analysis**: Processes 15+ validated genetic markers across multiple phenotypic categories
- **Real-time Processing**: Instant analysis and visualization of genetic variants
- **Privacy-Centric Architecture**: Zero-persistence processing model ensures data confidentiality
- **Research-Grade Interface**: Publication-quality visualizations with interactive exploration
- **Cross-Platform Compatibility**: Responsive design optimized for desktop, tablet, and mobile

---

## Features

### Core Functionality

**Intelligent File Processing**
- Drag-and-drop interface with real-time validation
- Support for 23andMe standard format (`.txt`, `.csv`)
- Automatic format detection and error handling
- File size optimization with 16MB upload limit

**Advanced Genetic Analysis**
- Multi-SNP genotype interpretation
- Evidence-based trait association mapping
- Risk stratification algorithms
- Confidence scoring for genetic predictions

**Interactive Visualization**
- Category-segmented results dashboard
- Color-coded significance indicators
- Detailed variant-level breakdowns
- Exportable reports for documentation

**Enterprise-Grade Security**
- Ephemeral data processing (no permanent storage)
- Filename sanitization and malware protection
- CORS-enabled secure API communication
- Input validation and type checking

---

## Technology Stack

### Frontend Architecture
```
React 18.2.0          Modern component-based UI framework
Axios                 Promise-based HTTP client
React Dropzone        File upload with drag-and-drop
CSS3                  Custom styling with gradient design system
```

### Backend Infrastructure
```
Flask 2.3.3           Lightweight WSGI web framework
Flask-CORS            Cross-origin resource sharing
Python 3.8+           Core processing engine
RESTful API           Standard HTTP methods and status codes
```

---

## Installation

### Prerequisites

Ensure the following are installed on your system:

- **Python** 3.8 or higher → [Download](https://python.org/downloads)
- **Node.js** 14 or higher → [Download](https://nodejs.org)
- **pip** (included with Python)
- **npm** (included with Node.js)

### Quick Start

#### 1. Clone the Repository

```bash
git clone <repository-url>
cd genomic-dashboard
```

#### 2. Backend Configuration

```bash
# Navigate to backend directory
cd backend

# Create isolated Python environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate sample datasets
python sample_data.py

# Launch backend server
python app.py
```

**Backend will be available at:** `http://localhost:5001`

#### 3. Frontend Configuration

Open a new terminal window:

```bash
# Navigate to frontend directory
cd frontend

# Install Node dependencies
npm install

# Start development server
npm start
```

**Frontend will be available at:** `http://localhost:3000`

---

## Project Structure

```
genomic-dashboard/
│
├── backend/
│   ├── app.py                    # Flask application server
│   ├── genomic_processor.py      # SNP analysis engine
│   ├── security.py               # Input validation & sanitization
│   ├── sample_data.py            # Test dataset generator
│   ├── requirements.txt          # Python dependencies
│   └── uploads/                  # Temporary file storage
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── FileUpload.js     # Upload interface component
│   │   │   ├── ReportDisplay.js  # Results visualization
│   │   │   └── TraitCard.js      # Individual trait cards
│   │   ├── App.js                # Root application component
│   │   ├── App.css               # Global styles
│   │   └── index.js              # Application entry point
│   ├── public/
│   │   └── index.html
│   └── package.json              # Node dependencies
│
└── README.md                     # Documentation
```

---


### Sample Data Format

Create test files using the 23andMe standard format:

```
# rsid    chromosome    position    genotype
rs1815739    11    66300000    CC
rs7495174    15    28000000    GG
rs9939609    16    53800000    TT
```

**Included Sample Files:**
- `test_dna.txt` - Basic validation dataset
- `athlete_dna.txt` - Endurance athlete profile
- `mixed_traits.txt` - Diverse genetic markers
- `power_athlete.txt` - Strength athlete profile

---

## Genetic Markers

### Categories and SNPs Analyzed

#### Athletic Performance & Fitness
| SNP ID | Gene | Trait | Significance |
|--------|------|-------|--------------|
| rs1815739 | ACTN3 | Muscle fiber composition | High |
| rs1049434 | MCT1 | Lactate transport capacity | Moderate |

#### Physical Characteristics
| SNP ID | Gene | Trait | Significance |
|--------|------|-------|--------------|
| rs7495174 | OCA2 | Eye color determination | High |
| rs12913832 | HERC2 | Eye color modifier | High |
| rs12896399 | SLC24A4 | Skin pigmentation | Moderate |
| rs1805007 | MC1R | Red hair & skin tone | High |
| rs12203592 | IRF4 | Hair color variation | Moderate |

#### Health & Metabolism
| SNP ID | Gene | Trait | Significance |
|--------|------|-------|--------------|
| rs9939609 | FTO | Weight regulation | High |
| rs17782313 | MC4R | Appetite control | Moderate |
| rs4680 | COMT | Stress response | Moderate |
| rs6265 | BDNF | Cognitive function | Moderate |

#### Nutrition & Circadian Biology
| SNP ID | Gene | Trait | Significance |
|--------|------|-------|--------------|
| rs4988235 | LCT | Lactose metabolism | High |
| rs1761667 | CD36 | Fat taste perception | Low |
| rs228697 | PER3 | Chronotype preference | Moderate |

---

### Educational Purpose Disclaimer

This platform is designed exclusively for **educational and research purposes**. The genetic insights provided should not be interpreted as:

- Medical diagnosis or clinical advice
- Treatment recommendations
- Professional genetic counseling
- Definitive health predictions

### Recommended Use Cases

- Bioinformatics education and training
- Understanding genetic inheritance patterns
- Full-stack web development learning
- Data visualization techniques exploration
- Research methodology demonstration

**For medical decisions involving genetic information, consult certified genetic counselors and healthcare professionals.**

---

## Contributing

We welcome contributions from the scientific and developer communities.

## Developer

**Shalini Singh**  
*Bioinformatics Engineer & Full-Stack Developer*

- 🔗 LinkedIn: [linkedin.com/in/shalinisingh](linkedin.com/in/shalinisingh)
- 💻 GitHub: [github.com/shalinisingh](https://github.com/singhshalini7545-dot)
- 🌐 Portfolio: [shalinisingh.dev](https://singhshalini7545-dot.github.io/portfolio/)
- 📧 Email: singhshalini6375@gmail.com

---

## Acknowledgments

This project synthesizes research from peer-reviewed genetic studies and open-source bioinformatics resources. Genetic variant interpretations are based on published scientific literature and population genetics databases.

---

<div align="center">

**Built with precision for the advancement of genomic education**

⭐ Star this repository if you find it valuable for your research or learning

</div>
