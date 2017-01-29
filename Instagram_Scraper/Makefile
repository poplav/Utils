.PHONY: dev

DEV_IMAGE:=jupyter/scipy-notebook

dev:
	@docker run -it --rm \
	-p 8888:8888 \
	-v `pwd`/notebooks:/home/jovyan/work \
	$(DEV_IMAGE)