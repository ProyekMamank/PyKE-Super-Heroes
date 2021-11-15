import contextlib
import sys

from pyke import knowledge_engine
from pyke import krb_traceback

engine = knowledge_engine.engine(__file__)


def bc_super_heroes():

    engine.reset()

    engine.activate('sh_rules')

    print("Asking questions...")
    
    try:
        with engine.prove_goal('sh_rules.hero_is($hero)') as gen: 
            for vars, plan in gen:
                print("Your Marvel Super Hero is: %s" % (vars['hero']))
    except Exception:
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("Finish :D")
    #engine.print_stats()

