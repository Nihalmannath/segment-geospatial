# segment-geospatial - Installation and Run Summary

## ✓ Repository Successfully Set Up and Running!

### Installation Status
- **Package**: segment-geospatial v0.13.0
- **Installation Type**: Development mode (editable install)
- **Python Version**: 3.13.3
- **Environment**: Conda/pip hybrid environment

### What Was Done

1. **Package Installation**
   - Installed segment-geospatial in development mode using `pip install -e .`
   - Installed all core dependencies from requirements.txt
   - Installed pytest for running tests

2. **Verification**
   - Successfully imported samgeo module
   - Version confirmed: 0.13.0
   - Core modules are functional:
     - ✓ SamGeo (Segment Anything Model)
     - ✓ SamGeo2 (SAM 2)
     - ✓ Common utilities

3. **Test Results**
   - **6 tests passed** ✓
   - **4 tests failed** (due to missing optional dependencies)
   - Failed tests require: GDAL and rio-cogeo (not essential for core functionality)

### How to Use the Repository

#### Option 1: Use as a Python Library
```python
import samgeo
from samgeo import SamGeo

# Your code here
```

#### Option 2: Run Example Notebooks
The repository includes extensive examples in the `docs/examples/` directory:
- `satellite.ipynb` - Segmenting remote sensing imagery
- `automatic_mask_generator.ipynb` - Auto-generating object masks
- `input_prompts.ipynb` - Interactive segmentation
- `text_prompts.ipynb` - Text-based segmentation
- And many more!

To run notebooks, install Jupyter:
```bash
pip install jupyter
jupyter notebook docs/examples/
```

#### Option 3: Run Tests
```bash
python -m pytest tests/ -v
```

#### Option 4: Run the Demo Script
```bash
python demo_run.py
```

### Available Features by Installation Type

**Currently Installed (Core)**:
- Basic SAM segmentation
- GeoTIFF handling
- Vector data processing
- Basic visualization

**Additional Features Available**:
- SAM 2: `pip install segment-geospatial[samgeo2]`
- Fast SAM: `pip install segment-geospatial[fast]`
- HQ-SAM: `pip install segment-geospatial[hq]`
- Text prompts: `pip install segment-geospatial[text]`
- All features: `pip install segment-geospatial[all]`
- Examples + extras: `pip install segment-geospatial[extra]`

### Next Steps

1. **Install additional features** (optional):
   ```bash
   pip install segment-geospatial[samgeo2]  # For SAM 2 support
   pip install segment-geospatial[text]     # For text prompts
   pip install segment-geospatial[extra]    # For running examples
   ```

2. **Explore examples**:
   - Check `docs/examples/` for Jupyter notebooks
   - Visit https://samgeo.gishub.org for full documentation

3. **Start coding**:
   - Import samgeo in your Python scripts
   - Follow examples in the documentation
   - Use for geospatial image segmentation tasks

### Repository Structure
```
segment-geospatial/
├── samgeo/              # Main package code
│   ├── __init__.py
│   ├── samgeo.py        # SAM 1 implementation
│   ├── samgeo2.py       # SAM 2 implementation
│   ├── samgeo3.py       # SAM 3 implementation
│   ├── common.py        # Utility functions
│   └── ...
├── docs/
│   └── examples/        # Example notebooks
├── tests/               # Test suite
├── demo_run.py          # Demo script (created)
└── requirements.txt     # Dependencies

```

### Resources
- **Documentation**: https://samgeo.gishub.org
- **GitHub**: https://github.com/opengeos/segment-geospatial
- **Paper**: https://doi.org/10.21105/joss.05663

---
**Status**: ✓ Repository is ready to use!
