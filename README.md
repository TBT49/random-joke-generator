# Random Joke Generator 🎭

A Python application that fetches random jokes from multiple external APIs and displays them in a fun, interactive way.

## Features ✨

- 🎭 **Multiple API Support**: Integrates with 5+ different joke APIs
- 🎲 **Random Joke Generation**: Get jokes on-demand
- 📂 **Category Support**: Filter jokes by category (Programming, Knock-Knock, etc.)
- 💾 **Save & Load**: Export and import joke collections
- 🔄 **Batch Processing**: Fetch multiple jokes at once
- 🖥️ **Interactive Menu**: Easy-to-use CLI interface
- ⚡ **CLI Mode**: Command-line usage for automation

## Supported APIs

| API | Type | Categories |
|-----|------|------------|
| **JokeAPI** | Comprehensive | Any, Miscellaneous, Programming, Knock-Knock, General, Christmas |
| **Random Joke API** | Simple | Single |
| **Official Joke API** | Two-part | Single |
| **Useless Facts** | Facts | Single |
| **Dad Joke API** | Dad Jokes | Single |

## Installation

```bash
# Clone the repository
git clone https://github.com/TBT49/random-joke-generator.git
cd random-joke-generator

# Install dependencies
pip install -r requirements.txt
```

## Quick Start

### Interactive Mode

```bash
python joke_generator.py
```

This launches an interactive menu where you can:
- Get a single random joke
- Get multiple jokes
- Get jokes by category
- Choose a specific API
- View available APIs
- Save jokes to a file
- Load jokes from a file

### CLI Mode

```bash
# Get a single joke
python joke_generator.py single

# Get 10 random jokes
python joke_generator.py multiple 10

# Get a joke from Programming category
python joke_generator.py category Programming
```

## Usage Examples

### Python Script

```python
from joke_generator import JokeGenerator

# Initialize generator
generator = JokeGenerator()

# Get single joke
joke = generator.get_joke()
print(joke)

# Get multiple jokes
jokes = generator.get_multiple_jokes(count=5)
for j in jokes:
    print(f"🎭 {j['joke']}\n")

# Get by category (JokeAPI only)
joke = generator.get_joke_category('Programming')
print(joke)

# Get from specific API
joke = generator.get_joke('dadjoke')
print(joke)

# Save jokes to file
generator.save_jokes_to_file(jokes, 'my_jokes.json')

# Load jokes from file
loaded = generator.load_jokes_from_file('my_jokes.json')
```

### Menu Navigation

```
1. Get a single joke - Fetches one random joke from any available API
2. Get multiple jokes - Batch fetch several jokes
3. Get by category - Fetch from specific category (Programming, Knock-Knock, etc.)
4. Choose API - Select a specific API source
5. View APIs - List all available APIs and their endpoints
6. Save jokes - Export fetched jokes to JSON file
7. Load jokes - Import previously saved jokes
```

## API Categories

**JokeAPI** supports these categories:
- `Any` - Mix of all categories
- `Miscellaneous` - General jokes
- `Programming` - Programming-related jokes
- `Knock-Knock` - Classic knock-knock jokes
- `General` - General humor
- `Christmas` - Holiday-themed jokes

## Output Format

Jokes are saved in JSON format:

```json
[
  {
    "id": 1,
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
    "timestamp": "2024-01-15T10:30:45.123456",
    "api": "dadjoke"
  }
]
```

## Error Handling

- **Network Timeout**: Automatically falls back to other APIs
- **API Unavailable**: Skips and tries the next API
- **Invalid Input**: User-friendly error messages

## Customization

You can modify the timeout and add more APIs:

```python
# Custom timeout
generator = JokeGenerator(timeout=10)

# Add new API to APIS dict
APIS['myapi'] = {
    'url': 'https://api.example.com/joke',
    'params': {'format': 'json'},
    'parser': 'parse_myapi'
}
```

## File Structure

```
random-joke-generator/
├── joke_generator.py      # Main application
├── requirements.txt       # Dependencies
├── README.md             # This file
├── QUICKSTART.md         # Quick start guide
├── jokes.json            # Saved jokes (generated)
└── .gitignore           # Git ignore rules
```

## Requirements

- Python 3.6+
- requests library
- Internet connection

## Performance Tips

- Use specific categories to speed up requests
- Cache jokes locally using save/load features
- Adjust timeout based on your connection speed
- Use CLI mode for scripting and automation

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No jokes fetched | Check internet connection, try another API |
| Slow response | Increase timeout value or use CLI mode |
| File not found | Ensure jokes.json exists in the directory |
| API error | API might be down, try another one |

## Contributing

Contributions are welcome! Feel free to:
- Add new joke APIs
- Improve parsers
- Add more categories
- Enhance the UI

## License

MIT License - Feel free to use this project for personal and commercial purposes.

## Disclaimer

This project is for educational and entertainment purposes. Jokes are fetched from public APIs and are subject to their respective licenses and terms of service.

## Credits

- JokeAPI - https://jokeapi.dev
- Official Joke API - https://official-joke-api.appspot.com
- Dad Joke API - https://icanhazdadjoke.com
- And other amazing public APIs!

---

**Have fun with jokes!** 🎉
