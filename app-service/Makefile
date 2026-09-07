IMAGE_NAME := app-service
TAG        ?= latest
ENV		   ?= dev


.PHONY: build test image deploy

build:
	@echo "Building the application..."
	python -m pip install -r requirements.txt
	python -m compileall .

test:build
	@echo "Running tests..."
	python -m pytest --maxfail=1 --disable-warnings -v

image:
	@echo "Building Docker image with TAG=$(TAG)..."
	docker build -t $(IMAGE_NAME):$(TAG) .

deploy: image
	@echo "Deploying to ENV=$(ENV) with TAG=$(TAG)..." 
	./scripts/deploy.sh $(ENV) $(IMAGE_NAME):$(TAG)