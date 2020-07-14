
# Idk some benchmarks or something

## Running

```bash
python slots.py
```

## output on 16gb i7 w/ cpu set to "performance"

```bash
normal_ns=519323.207                    
slots_ns=429898.147
slots_ns=415046.986
normal_ns=605717.807
```

# Conclusion

Slots gives us a `~30%` performance gain, and according to
https://pythonspeed.com/articles/python-object-memory/
it should also give pretty good memory usage improvements.


