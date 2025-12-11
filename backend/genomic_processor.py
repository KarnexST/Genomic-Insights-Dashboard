import csv
import json

class GenomicProcessor:
    def __init__(self):
        self.trait_database = self.load_trait_database()
    
    def load_trait_database(self):
        # EXPANDED Educational database of SNPs and traits
        return {
            # Athletic Performance SNPs
            'rs1815739': {
                'gene': 'ACTN3',
                'trait': 'Muscle Fiber Type',
                'genotype_effects': {
                    'CC': 'Enhanced endurance performance - Marathon runner type',
                    'CT': 'Mixed fiber type - Balanced athlete',
                    'TT': 'Enhanced power performance - Sprinter type'
                },
                'category': 'Fitness',
                'significance': 'High'
            },
            'rs1049434': {
                'gene': 'MCT1',
                'trait': 'Lactate Transport',
                'genotype_effects': {
                    'TT': 'Efficient lactate clearance - Good endurance',
                    'TA': 'Moderate lactate clearance',
                    'AA': 'Less efficient lactate clearance'
                },
                'category': 'Fitness',
                'significance': 'Moderate'
            },
            
            # Physical Traits SNPs
            'rs7495174': {
                'gene': 'OCA2',
                'trait': 'Eye Color Probability',
                'genotype_effects': {
                    'AA': 'Higher probability of brown eyes',
                    'AG': 'Mixed eye color probability',
                    'GG': 'Higher probability of blue/green eyes'
                },
                'category': 'Physical Traits',
                'significance': 'High'
            },
            'rs12913832': {
                'gene': 'HERC2',
                'trait': 'Eye Color',
                'genotype_effects': {
                    'AA': 'High probability of brown eyes',
                    'AG': 'Mixed eye color - Hazel/Green',
                    'GG': 'High probability of blue eyes'
                },
                'category': 'Physical Traits',
                'significance': 'High'
            },
            'rs12896399': {
                'gene': 'SLC24A4',
                'trait': 'Skin Pigmentation',
                'genotype_effects': {
                    'GG': 'Lighter skin tone',
                    'GT': 'Medium skin tone',
                    'TT': 'Darker skin tone'
                },
                'category': 'Physical Traits',
                'significance': 'Moderate'
            },
            
            # Metabolism & Weight SNPs
            'rs9939609': {
                'gene': 'FTO',
                'trait': 'Weight Management',
                'genotype_effects': {
                    'AA': 'Higher predisposition to obesity',
                    'AT': 'Moderate weight management risk',
                    'TT': 'Lower risk of obesity'
                },
                'category': 'Metabolism',
                'significance': 'High'
            },
            'rs17782313': {
                'gene': 'MC4R',
                'trait': 'Appetite Regulation',
                'genotype_effects': {
                    'CC': 'Higher appetite, increased BMI',
                    'CT': 'Moderate appetite regulation',
                    'TT': 'Better appetite control'
                },
                'category': 'Metabolism',
                'significance': 'Moderate'
            },
            
            # Neurology & Stress SNPs
            'rs4680': {
                'gene': 'COMT',
                'trait': 'Stress Response',
                'genotype_effects': {
                    'AA': 'Better stress resilience - Warrior type',
                    'AG': 'Moderate stress response',
                    'GG': 'Higher anxiety predisposition - Worrier type'
                },
                'category': 'Neurology',
                'significance': 'High'
            },
            'rs6265': {
                'gene': 'BDNF',
                'trait': 'Memory & Learning',
                'genotype_effects': {
                    'CC': 'Standard memory function',
                    'CT': 'Enhanced memory formation',
                    'TT': 'Better learning capacity'
                },
                'category': 'Neurology',
                'significance': 'Moderate'
            },
            
            # Food Response SNPs
            'rs4988235': {
                'gene': 'LCT',
                'trait': 'Lactose Tolerance',
                'genotype_effects': {
                    'AA': 'Lactose tolerant',
                    'AG': 'Partial lactose tolerance',
                    'GG': 'Lactose intolerant'
                },
                'category': 'Nutrition',
                'significance': 'High'
            },
            'rs1761667': {
                'gene': 'CD36',
                'trait': 'Fat Taste Sensitivity',
                'genotype_effects': {
                    'AA': 'High fat taste sensitivity',
                    'AG': 'Moderate fat sensitivity',
                    'GG': 'Low fat taste sensitivity'
                },
                'category': 'Nutrition',
                'significance': 'Moderate'
            },
            
            # Sleep & Circadian Rhythm
            'rs228697': {
                'gene': 'PER3',
                'trait': 'Sleep Pattern',
                'genotype_effects': {
                    'CC': 'Evening person - Night owl',
                    'CG': 'Flexible sleep pattern',
                    'GG': 'Morning person - Early riser'
                },
                'category': 'Sleep',
                'significance': 'Moderate'
            },
            
            # Additional Common SNPs
            'rs1805007': {
                'gene': 'MC1R',
                'trait': 'Red Hair & Fair Skin',
                'genotype_effects': {
                    'CC': 'Lower red hair probability',
                    'CT': 'Carrier of red hair variant',
                    'TT': 'Higher red hair probability'
                },
                'category': 'Physical Traits',
                'significance': 'Moderate'
            },
            'rs12203592': {
                'gene': 'IRF4',
                'trait': 'Hair Color',
                'genotype_effects': {
                    'CC': 'Darker hair likely',
                    'CT': 'Medium brown hair',
                    'TT': 'Blonde hair more likely'
                },
                'category': 'Physical Traits',
                'significance': 'Moderate'
            }
        }
    
    def process_23andme_file(self, filepath):
        """Process 23andMe format file without pandas"""
        results = {
            'traits': [],
            'health_risks': [],
            'nutrition': [],
            'sleep': [],
            'summary': {}
        }
        
        try:
            analyzed_snps = 0
            total_snps = 0
            
            with open(filepath, 'r') as file:
                for line in file:
                    # Skip comment lines
                    if line.startswith('#'):
                        continue
                    
                    # Skip empty lines
                    if not line.strip():
                        continue
                    
                    total_snps += 1
                    
                    # Split by tab or space
                    parts = line.strip().split()
                    if len(parts) >= 4:
                        rsid = parts[0]
                        genotype = parts[3]
                        
                        if rsid in self.trait_database:
                            snp_info = self.trait_database[rsid].copy()
                            snp_info['your_genotype'] = genotype
                            snp_info['interpretation'] = self.trait_database[rsid]['genotype_effects'].get(
                                genotype, 'Variant detected - interpretation not available'
                            )
                            
                            # Categorize properly
                            category = snp_info['category']
                            if category in ['Metabolism', 'Neurology']:
                                results['health_risks'].append(snp_info)
                            elif category == 'Nutrition':
                                results['nutrition'].append(snp_info)
                            elif category == 'Sleep':
                                results['sleep'].append(snp_info)
                            else:
                                results['traits'].append(snp_info)
                            
                            analyzed_snps += 1
            
            results['summary'] = {
                'total_snps_analyzed': total_snps,
                'traits_found': len(results['traits']),
                'health_risks_found': len(results['health_risks']),
                'nutrition_found': len(results['nutrition']),
                'sleep_found': len(results['sleep']),
                'matched_snps': analyzed_snps
            }
            
        except Exception as e:
            raise Exception(f"Error processing file: {str(e)}")
        
        return results
    
    def process_genomic_file(self, filepath):
        return self.process_23andme_file(filepath)

# Global instance
processor = GenomicProcessor()

def process_genomic_file(filepath):
    return processor.process_genomic_file(filepath)
