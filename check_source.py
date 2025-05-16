import inspect, sys, os, importlib
sys.path.insert(0, os.path.abspath('PyFrac-master/src'))
import multifracture_controller as mc
print(inspect.getsource(mc.MultifractureController._update_stress_shadow)) 