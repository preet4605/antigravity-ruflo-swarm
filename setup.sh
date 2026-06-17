#!/bin/bash
set -e

echo "Installing Ruflo Swarm and 134+ Specialized Agents for Antigravity CLI..."

TARGET_DIR="$HOME/.agents"

# Create directories if they don't exist
mkdir -p "$TARGET_DIR/skills"

# Copy all skills, agents, workflows, and rules
for dir in skills agents workflows rules; do
  if [ -d "./$dir" ]; then
    mkdir -p "$TARGET_DIR/$dir"
    cp -r ./$dir/* "$TARGET_DIR/$dir/"
    echo "✅ Installed items from $dir/"
  fi
done

# Copy the registry and builder
cp ./agent_registry.md "$TARGET_DIR/"
cp ./build_registry.py "$HOME/"
echo "✅ Installed the Swarm Agent Registry and builder script."

echo ""
echo "🎉 Installation complete!"
echo "To trigger the swarm, tell Antigravity in the chat:"
echo "'Read the ~/.agents/skills/ruflo-swarm/SKILL.md file and build [your idea] using the swarm.'"
