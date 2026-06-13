# Confluence Storage Patterns

Use these snippets when generating Confluence storage-format bodies. Replace placeholder values before publishing.

## Table Of Contents

```xml
<ac:structured-macro ac:name="toc">
  <ac:parameter ac:name="maxLevel">3</ac:parameter>
</ac:structured-macro>
```

## SVG-Only Two-Pane Diagram

Use this when the user asks for one image, SVG output, or no duplicate rendered image formats.

```xml
<table data-layout="wide"><tbody>
<tr><th><p>Mermaid source</p></th><th><p>Rendered SVG</p></th></tr>
<tr>
<td>
<ac:structured-macro ac:name="code" ac:schema-version="1">
<ac:parameter ac:name="language">mermaid</ac:parameter>
<ac:plain-text-body><![CDATA[flowchart LR
  A --> B]]></ac:plain-text-body>
</ac:structured-macro>
</td>
<td>
<ac:image ac:width="760">
<ri:attachment ri:filename="diagram.svg" />
</ac:image>
</td>
</tr>
</tbody></table>
```

## PNG Preview Plus SVG Attachment

Use this only when inline SVG rendering is unreliable or the user wants both preview and vector copy.

```xml
<table data-layout="wide"><tbody>
<tr><th><p>Mermaid source</p></th><th><p>Rendered image</p></th></tr>
<tr>
<td>
<ac:structured-macro ac:name="code" ac:schema-version="1">
<ac:parameter ac:name="language">mermaid</ac:parameter>
<ac:plain-text-body><![CDATA[flowchart LR
  A --> B]]></ac:plain-text-body>
</ac:structured-macro>
</td>
<td>
<ac:image ac:width="760">
<ri:attachment ri:filename="diagram.png" />
</ac:image>
<p>
<ac:link>
<ri:attachment ri:filename="diagram.svg" />
<ac:plain-text-link-body><![CDATA[Open SVG attachment]]></ac:plain-text-link-body>
</ac:link>
</p>
</td>
</tr>
</tbody></table>
```

## Full-Width Property

Set max/full width through the page content property:

```json
{
  "key": "content-appearance-published",
  "value": "full-width"
}
```

If the property already exists, update it with a new `version.number`. Verify by reading the property back and checking that `value` is `full-width`.

## Readback Checklist

- Page title and first heading match the requested title policy.
- Expected attachment filenames exist in `/child/attachment?expand=version,metadata`.
- Storage body contains the Mermaid source macro.
- Storage body contains embedded attachment references for the rendered image.
- Replaced legacy sections are absent.
- `content-appearance-published` is `full-width` when max width was requested.
