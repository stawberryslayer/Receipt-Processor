# Receipt-Processor

## Project structure
```
receipt-processor/
├── app/
│   ├── main.py
│   └── processor.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## Get Started
```bash
pip install -r requirements.txt
docker build -t receipt-processor .
docker run -p 8000:8000 receipt-processor