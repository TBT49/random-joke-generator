# Quick Start Guide 🚀

## 60 Second Setup

```bash
# 1. Clone repository
git clone https://github.com/TBT49/random-joke-generator.git
cd random-joke-generator

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python joke_generator.py
```

## Usage

### Get a Single Joke
```bash
python joke_generator.py single
```

### Get 5 Random Jokes
```bash
python joke_generator.py multiple 5
```

### Get Programming Jokes
```bash
python joke_generator.py category Programming
```

### Interactive Menu
```bash
python joke_generator.py
```

Then choose from the menu:
```
1. Get a single joke
2. Get multiple jokes (specify count)
3. Get jokes by category
4. Choose specific API
5. View all APIs
6. Save jokes to file
7. Load jokes from file
```

## Python Usage

```python
from joke_generator import JokeGenerator

generator = JokeGenerator()

# Single joke
joke = generator.get_joke()
print(joke)

# Multiple jokes
jokes = generator.get_multiple_jokes(10)

# By category
joke = generator.get_joke_category('Programming')

# Specific API
joke = generator.get_joke('dadjoke')

# Save to file
generator.save_jokes_to_file(jokes, 'my_jokes.json')
```

## Available APIs

- `jokapi` - Comprehensive joke API with categories
- `random_joke` - Simple random jokes
- `official_joke` - Official joke API
- `uselessfacts` - Useless but fun facts
- `dadjoke` - Classic dad jokes

## Categories (JokeAPI only)

- Any
- Programming
- Miscellaneous
- Knock-Knock
- General
- Christmas

## Tips

✨ **Best for beginners**: Use menu mode (no CLI args)

⚡ **For automation**: Use CLI mode with specific parameters

💾 **Save for later**: Use save/load features to cache jokes

🔄 **Batch processing**: Get multiple jokes and save them

---

Enjoy! 🎭
