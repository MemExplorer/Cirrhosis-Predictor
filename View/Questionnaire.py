#!python
import os.path
import sys
parent_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parent_dir)
from Model.RenderHelper import RenderHelper

RenderHelper.render_page("..\ViewModel\Questionnaire1.html")