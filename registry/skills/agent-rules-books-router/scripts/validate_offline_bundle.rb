#!/usr/bin/env ruby
# frozen_string_literal: true

require "yaml"

ROOT = File.expand_path("..", __dir__)

EXPECTED_RULES = [
  "a-philosophy-of-software-design/a-philosophy-of-software-design",
  "clean-architecture/clean-architecture",
  "clean-code/clean-code",
  "code-complete/code-complete",
  "designing-data-intensive-applications/designing-data-intensive-applications",
  "domain-driven-design/domain-driven-design",
  "domain-driven-design-distilled/domain-driven-design-distilled",
  "implementing-domain-driven-design/implementing-domain-driven-design",
  "patterns-of-enterprise-application-architecture/patterns-of-enterprise-application-architecture",
  "refactoring/refactoring",
  "refactoring-guru/refactoring-guru",
  "release-it/release-it",
  "the-pragmatic-programmer/the-pragmatic-programmer",
  "working-effectively-with-legacy-code/working-effectively-with-legacy-code"
].freeze

REQUIRED_DOCS = [
  "references/upstream/README.md",
  "references/upstream/LICENSE",
  "references/upstream/docs/USAGE.md",
  "references/upstream/docs/COMPATIBILITY.md",
  "references/source-index.md"
].freeze

def fail_with(message)
  warn "FAIL: #{message}"
  exit 1
end

skill = File.read(File.join(ROOT, "SKILL.md"))
frontmatter = skill[/\A---\n(.*?)\n---\n/m, 1]
fail_with("SKILL.md frontmatter missing") unless frontmatter

metadata = YAML.safe_load(frontmatter)
fail_with("name must be agent-rules-books-router") unless metadata["name"] == "agent-rules-books-router"
fail_with("description must start with Use when") unless metadata["description"].to_s.start_with?("Use when")

missing = []
REQUIRED_DOCS.each do |path|
  missing << path unless File.file?(File.join(ROOT, path))
end

EXPECTED_RULES.each do |base|
  missing << "references/upstream/#{base}.mini.md" unless File.file?(File.join(ROOT, "references/upstream/#{base}.mini.md"))
  missing << "references/upstream/#{base}.nano.md" unless File.file?(File.join(ROOT, "references/upstream/#{base}.nano.md"))
  missing << "references/upstream/#{base}.md" unless File.file?(File.join(ROOT, "references/upstream/#{base}.md"))
end

fail_with("missing files: #{missing.join(', ')}") unless missing.empty?

runtime_refs = skill.scan(%r{references/upstream/[^\s`)]+}).uniq
runtime_missing = runtime_refs.reject { |path| File.file?(File.join(ROOT, path)) }
fail_with("runtime references missing: #{runtime_missing.join(', ')}") unless runtime_missing.empty?

puts "PARSE_OK"
puts "OFFLINE_BUNDLE_OK"
puts "rule_sets=#{EXPECTED_RULES.length}"
puts "rule_files=#{EXPECTED_RULES.length * 3}"
