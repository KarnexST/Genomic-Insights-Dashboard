import React, { useState } from 'react';
import FileUpload from './components/FileUpload';
import ReportDisplay from './components/ReportDisplay';
import './App.css';

function App() {
  const [report, setReport] = useState(null);
  const [loading, setLoading] = useState(false);

  return (
    <div className="App">
      <header className="app-header">
        <h1>Genomic Insights Dashboard</h1>
        <p>Advanced DNA Analysis Platform for Personalized Genetic Insights</p>
      </header>
      
      <main>
        {!report ? (
          <FileUpload 
            setReport={setReport} 
            loading={loading} 
            setLoading={setLoading} 
          />
        ) : (
          <ReportDisplay 
            report={report} 
            onReset={() => setReport(null)} 
          />
        )}
      </main>
      
      <footer>
        <div className="footer-container">
          {/* About Section */}
          <div className="footer-section">
            <h3>About Genomic Insights</h3>
            <p>
              A sophisticated platform for analyzing genetic data, providing 
              personalized insights into traits, wellness markers, and ancestral 
              heritage through advanced computational biology.
            </p>
            <div className="disclaimer-box">
              <p>
                <strong>Note:</strong> This tool provides educational insights based 
                on genetic research. Results are for informational purposes and 
                should not be considered medical advice. Always consult healthcare 
                professionals for medical decisions.
              </p>
            </div>
          </div>
          
          {/* Quick Links */}
          <div className="footer-section">
            <h3>Quick Links</h3>
            <ul className="footer-links">
              <li>
                <a href="#upload">
                  <i>📊</i> Upload DNA Data
                </a>
              </li>
              <li>
                <a href="#analysis">
                  <i>🔬</i> Analysis Methods
                </a>
              </li>
              <li>
                <a href="#research">
                  <i>📚</i> Research Database
                </a>
              </li>
              <li>
                <a href="#privacy">
                  <i>🔒</i> Privacy Policy
                </a>
              </li>
            </ul>
          </div>
          
{/* Developer Section */}
<div className="footer-section">
  <h3>Project Developer</h3>
  <div className="developer-info">
    <div className="developer-name">Shalini Singh</div>
    <div className="developer-title">Bioinformatics Engineer & Full-Stack Developer</div>
    
    <div className="social-links-vertical">
      <a 
        href="https://www.linkedin.com/in/shalinisingh" 
        target="_blank" 
        rel="noopener noreferrer"
        className="social-link-vertical"
      >
        <span className="social-icon linkedin-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/>
          </svg>
        </span>
        <span>LinkedIn Profile</span>
      </a>
      
      <a 
        href="https://github.com/singhshalini7545-dot" 
        target="_blank" 
        rel="noopener noreferrer"
        className="social-link-vertical"
      >
        <span className="social-icon github-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
          </svg>
        </span>
        <span>GitHub Repository</span>
      </a>
      
      <a 
        href="https://singhshalini7545-dot.github.io/portfolio" 
        target="_blank" 
        rel="noopener noreferrer"
        className="social-link-vertical"
      >
        <span className="social-icon portfolio-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M21 13v10h-6v-6h-6v6h-6v-10h-3l12-12 12 12h-3zm-1-5.907v-5.093h-3v2.093l3 3z"/>
          </svg>
        </span>
        <span>Portfolio Website</span>
      </a>
      
      <a 
        href="singhshalini6375@gmail.com" 
        className="social-link-vertical"
      >
        <span className="social-icon email-icon">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
            <path d="M0 3v18h24v-18h-24zm21.518 2l-9.518 7.713-9.518-7.713h19.036zm-19.518 14v-11.817l10 8.104 10-8.104v11.817h-20z"/>
          </svg>
        </span>
        <span>Contact Email</span>
      </a>
    </div>
  </div>
</div>

          
          {/* Technology Stack */}
          <div className="footer-section">
            <h3>Technology Stack</h3>
            <ul className="footer-links">
              <li>
                <a href="#">
                  <i>⚛️</i> React.js
                </a>
              </li>
              <li>
                <a href="#">
                  <i>🐍</i> Python Flask
                </a>
              </li>
              <li>
                <a href="#">
                  <i>🧬</i> BioPython
                </a>
              </li>
              <li>
                <a href="#">
                  <i>📊</i> Data Visualization
                </a>
              </li>
            </ul>
          </div>
        </div>
        
        <div className="footer-bottom">
          <div className="legal-links">
            <a href="#privacy">Privacy Policy</a>
            <a href="#terms">Terms of Service</a>
            <a href="#cookies">Cookie Policy</a>
            <a href="#data">Data Processing</a>
            <a href="#contact">Contact</a>
          </div>
          
          <div className="copyright">
            © {new Date().getFullYear()} Genomic Insights Dashboard. 
            All rights reserved. 
            <br />
            Developed with ❤️ by Shalini Singh
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
